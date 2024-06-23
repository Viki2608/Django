from django.http import HttpResponse
from django.shortcuts import render
import jenkins
from .forms import PipelineForm, GroupDeploy
def cicd(request):
    nav_items = [
        {'url': '#', 'icon': 'bx-grid-alt', 'name': 'Dashboard', 'tooltip': 'Dashboard'},
        {'url': '#', 'icon': 'bx-user', 'name': 'User', 'tooltip': 'User'},
        {'url': 'group_deploy', 'icon': 'bx-chat', 'name': 'Group Deploy', 'tooltip': 'Group Deploy'},
        {'url': 'cicd', 'icon': 'bx-folder', 'name': 'cicd', 'tooltip': 'CI/CD'},
        {'url': '#', 'icon': 'bx-heart', 'name': 'Saved', 'tooltip': 'Saved'},
    ]
    form = PipelineForm()
    user = request.user
    user = "vicky"
    context = {
        'form': form,
        'nav_items': nav_items,
        'user': user,
    }
    return render(request, "cicd/index.html", context)

def group_deploy(request):
    nav_items = [
        {'url': '#', 'icon': 'bx-grid-alt', 'name': 'Dashboard', 'tooltip': 'Dashboard'},
        {'url': '#', 'icon': 'bx-user', 'name': 'User', 'tooltip': 'User'},
        {'url': 'group_deploy', 'icon': 'bx-chat', 'name': 'Group Deploy', 'tooltip': 'Group Deploy'},
        {'url': 'cicd', 'icon': 'bx-folder', 'name': 'cicd', 'tooltip': 'CI/CD'},
        {'url': '#', 'icon': 'bx-heart', 'name': 'Saved', 'tooltip': 'Saved'},
    ]
    form = GroupDeploy()
    user = request.user
    user = "vicky"
    context = {
        'form': form,
        'nav_items': nav_items,
        'user': user,
    }
    return render(request, "groupdeploy/index.html", context)

def process_form(request):
    if request.method == 'POST':
        form = PipelineForm(request.POST)
        if form.is_valid():
            organization = form.cleaned_data['organization']
            repository = form.cleaned_data['repository']
            branch = form.cleaned_data['branch']
            job_name = f"{organization}_{repository}_{branch}"
            
            try:
                # Connect to Jenkins (replace with your Jenkins URL and credentials)
                server = jenkins.Jenkins('http://localhost:8080/', username='admin', password='admin')
                
                # Create Jenkins job
                job_config = f'''
                <project>
                    <actions/>
                    <description>Automatically generated job for {organization}/{repository}</description>
                    <keepDependencies>false</keepDependencies>
                    <properties/>
                    <scm class="hudson.scm.NullSCM"/>
                    <canRoam>true</canRoam>
                    <disabled>false</disabled>
                    <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
                    <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
                    <triggers/>
                    <concurrentBuild>false</concurrentBuild>
                    <builders/>
                    <publishers/>
                    <buildWrappers/>
                </project>
                '''
                
                server.create_job(job_name, job_config)
                
                return HttpResponse(f'Jenkins job "{job_name}" created successfully!')
            
            except jenkins.JenkinsException as e:
                return HttpResponse(f'Failed to create Jenkins job: {str(e)}')
        
        else:
            return HttpResponse('Form is not valid')
    
    else:
        # If not a POST request, handle as needed (e.g., redirect or error response)
        return HttpResponse('Method not allowed')

