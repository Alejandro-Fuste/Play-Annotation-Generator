# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_185`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_185/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 34 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-97] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [111-117] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [91-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [112-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [116-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-103] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-84] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' for track '18' starts at frame 120, but the player has no visible bounding box on this frame.
> - Action 'Action_SackQuarterback' range [120-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-120] for track '21' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.