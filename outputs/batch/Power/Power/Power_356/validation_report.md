# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_356`
- **Input XML**: `outputs/batch/Power/Power/Power_356/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [11-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-123] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-131] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-158] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-163] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-188] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-199] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-98] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-162] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-181] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-94] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-214] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-232] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-238] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [89-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [101-123] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [128-129] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-148] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-137] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-145] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-220] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-237] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-205] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-83] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-90] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-102] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-18] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-38] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-46] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-126] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-80] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-98] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-104] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-103] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-164] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [89-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-194] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-130] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-142] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-163] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-160] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-170] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-146] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-124] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-145] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-161] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-184] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-150] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-190] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-159] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-170] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-181] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-187] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-196] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-203] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-209] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-236] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-217] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-225] for track '30' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.