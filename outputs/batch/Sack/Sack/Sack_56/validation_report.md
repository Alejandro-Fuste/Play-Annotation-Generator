# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_56`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_56/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
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
> - Action 'Action_PreSnap' range [0-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [77-86] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' for track '1' starts at frame 90, but the player has no visible bounding box on this frame.
> - Action 'Action_SackQuarterback' range [90-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [87-88] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-90] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-69] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-90] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-90] for track '19' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.