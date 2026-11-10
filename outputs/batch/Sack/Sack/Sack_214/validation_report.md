# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_214`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_214/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 39 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_CloseOnQuarterback' at frame 74 targets track ID '', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-101] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-116] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [93-97] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-80] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-95] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [110-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [119-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-36] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-120] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-120] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.