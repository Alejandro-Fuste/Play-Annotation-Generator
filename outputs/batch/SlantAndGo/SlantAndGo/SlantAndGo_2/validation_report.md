# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SlantAndGo_2`
- **Input XML**: `outputs/batch/SlantAndGo/SlantAndGo/SlantAndGo_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SlantAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [8–26], lower_priority='Action_PassBlock' annotated_start=18, effective_Action_PassBlock_start=27.
> - Action 'Action_None' range [8-65] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-224] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-124] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [127-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [159-161] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [180-182] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [184-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-202] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-26] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [33-34] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-47] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-13] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-57] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-133] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-131] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-141] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [143-153] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [155-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-82] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [8-12] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [91-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-114] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [8-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-151] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [8-26] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-89] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [107-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [116-239] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-15] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [57-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-107] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-219] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-227] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-160] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-154] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-218] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-190] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-239] for track '23' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.