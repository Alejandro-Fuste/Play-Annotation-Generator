# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_29`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_29/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 52: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_SecureCatch' for track '3' has invalid range: start=181, end=178. Clamping end to start.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [32–39], lower_priority='Action_RunBlock' annotated_start=39, effective_Action_RunBlock_start=40.
> - Segment 'Action_ThrowPass' for track '17' has invalid range: start=127, end=73. Clamping end to start.
> - Action 'Action_None' range [144-202] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [32-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-178] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-185] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-65] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-99] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-83] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-94] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-210] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [32-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-192] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-201] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [40-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [52-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [64-99] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [105-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-73] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [39-45] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [65-210] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [39-192] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [195-204] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [208-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [39-83] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [92-95] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [102-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-80] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-200] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [198-204] for track '25' has 2 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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