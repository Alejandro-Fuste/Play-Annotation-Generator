# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_176`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_176/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 47 |
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
> - Action 'Action_PreSnap' range [0-26] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' for track '2' starts at frame 90, but the player has no visible bounding box on this frame.
> - Action 'Action_SackQuarterback' range [90-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-61] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-90] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-10] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-55] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-90] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-70] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-20] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-23] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-90] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-22] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-26] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [63-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-40] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-52] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-56] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-90] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [63-83] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [86-90] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-86] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-90] for track '26' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.