# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_71`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_71/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [72–86], lower_priority='Action_PassBlock' annotated_start=75, effective_Action_PassBlock_start=87.
> - Action 'Action_None' range [72-238] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [126-128] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-139] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-103] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [72-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-138] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-142] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [111-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [133-226] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-110] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-92] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-121] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-235] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-167] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-186] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '29' has 1 frames without a visible bounding box.
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
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.