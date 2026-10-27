# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_54`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_54/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [35-64] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-84] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-94] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [45-71] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [76-165] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [167-180] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-113] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [40-70] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [78-124] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-65] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-111] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-56] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-74] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-37] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-37] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-50] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-66] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-141] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-167] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-180] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-180] for track '24' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.