# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_79`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_79/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 47 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 160: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-87] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [110-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-120] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' for track '6' starts at frame 75, but the player has no visible bounding box on this frame.
> - Action 'Action_CloseOnQuarterback' range [75-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [77-78] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [80-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-74] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-67] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-72] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-120] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-57] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-113] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-120] for track '25' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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