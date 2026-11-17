# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_342`
- **Input XML**: `outputs/batch/Power/Power/Power_342/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 683: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [18-194] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-227] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-209] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-247] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-259] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [129-147] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-162] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-195] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-180] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-196] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [129-146] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [152-165] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-234] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-142] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-238] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-193] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-169] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-250] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-195] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-137] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-43] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-138] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-167] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-166] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-172] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-192] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-206] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-185] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-146] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-203] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-217] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-181] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-186] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-233] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-171] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-195] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-186] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-206] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-216] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-191] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-225] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-223] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-246] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-262] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-258] for track '29' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.