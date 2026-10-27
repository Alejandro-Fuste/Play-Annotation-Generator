# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_53`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 108: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [90-238] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [97-164] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [171-182] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [130-238] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [97-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-154] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [156-238] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-220] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-161] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-239] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [90-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-155] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-221] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-181] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-224] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-236] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [97-116] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-9] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-29] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-201] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-214] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-231] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-227] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-231] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-239] for track '30' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.