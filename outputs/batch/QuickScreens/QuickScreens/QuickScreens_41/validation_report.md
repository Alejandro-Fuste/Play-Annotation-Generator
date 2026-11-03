# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_41`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 128 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 46: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [16-115] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-91] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-137] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-171] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [173-193] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [73-130] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [132-145] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-193] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [27-122] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-131] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-53] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-59] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-65] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-93] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-112] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-58] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-193] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-47] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-25] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-52] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-83] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-193] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [16-35] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-42] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-60] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-113] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [16-193] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-193] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-76] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-119] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-167] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-30] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-72] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-93] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-139] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-179] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-187] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-41] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-89] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-193] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-193] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-76] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-145] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-153] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-193] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-25] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-58] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-183] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-193] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-62] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-151] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-193] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-178] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-193] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-152] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-176] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-193] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-193] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '44' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.