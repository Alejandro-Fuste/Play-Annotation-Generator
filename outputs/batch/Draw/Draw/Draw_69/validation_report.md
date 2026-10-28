# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_69`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_69/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 137: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [36–54], lower_priority='Action_PassBlock' annotated_start=39, effective_Action_PassBlock_start=55.
> - Action 'Action_None' range [36-236] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-112] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-129] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-69] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-112] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-219] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-231] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-127] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-89] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-168] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-218] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [220-234] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [77-130] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-224] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-87] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-77] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-64] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-158] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '24' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.