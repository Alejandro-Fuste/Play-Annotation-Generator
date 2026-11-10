# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_142`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_142/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 39 |
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
> - Action 'Action_PreSnap' range [0-118] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [88-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '14' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [74-87] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-78] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [105-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-118] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.