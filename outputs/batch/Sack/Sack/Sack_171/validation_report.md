# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_171`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_171/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-92] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-99] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-166] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-203] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-197] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [100-148] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [153-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-105] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [90-94] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-13] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-45] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-61] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-54] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-58] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-68] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-61] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-91] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-134] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-156] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-73] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-140] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-100] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-132] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-142] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-101] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-144] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-195] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-201] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-202] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-205] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '26' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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