# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_151`
- **Input XML**: `outputs/batch/Power/Power/Power_151/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 304: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [21-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-197] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-210] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-210] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-97] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-136] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-168] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-97] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-140] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-145] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-132] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-155] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-105] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [72-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-64] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-74] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-142] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-210] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-174] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-118] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-155] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-164] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-173] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-184] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-193] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-205] for track '34' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.