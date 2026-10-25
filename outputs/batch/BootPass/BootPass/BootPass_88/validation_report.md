# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_88`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_88/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [27–42], lower_priority='Action_RunBlock' annotated_start=35, effective_Action_RunBlock_start=43.
> - Action 'Action_None' range [27-167] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-80] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-161] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [35-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [35-181] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-116] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [35-48] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [50-131] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [134-135] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [148-165] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-47] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-50] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-74] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-106] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-224] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [35-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [134-173] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-69] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-173] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [43-59] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-35] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-37] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-66] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-31] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-62] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-238] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-47] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-107] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-60] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-176] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-131] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-117] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-234] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-148] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-154] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-168] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.