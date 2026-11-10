# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_98`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_98/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
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
> - Action 'Action_PreSnap' range [0-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [63-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [87-89] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-54] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-62] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [89-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-15] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-66] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-7] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-37] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-65] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-90] for track '22' has 2 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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