# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_61`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_61/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 45 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [140-141] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [154-160] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [166-169] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [114-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [146-151] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [162-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-91] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [103-111] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-180] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-148] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-159] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-166] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-180] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.