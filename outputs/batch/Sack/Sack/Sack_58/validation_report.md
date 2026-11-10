# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_58`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_58/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 36 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-69] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-81] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-89] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-78] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-101] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-83] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [97-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-88] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-119] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-109] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [117-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-120] for track '22' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.