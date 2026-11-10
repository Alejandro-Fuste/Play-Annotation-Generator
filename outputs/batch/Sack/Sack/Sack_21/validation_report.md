# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_21`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_21/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-84] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-50] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-60] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [72-77] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [79-81] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [82-83] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' for track '4' starts at frame 90, but the player has no visible bounding box on this frame.
> - Action 'Action_SackQuarterback' range [90-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-80] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-90] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-76] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-41] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-47] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-90] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-64] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-90] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-86] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-90] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '25' has 1 frames without a visible bounding box.
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