# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_207`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_207/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 31 |
| Ball Tracks | 2 |
| CSV events parsed | 19 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Segment 'Action_SnapReceive' for track '17' has invalid range: start=359, end=61. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '17' has invalid range: start=359, end=74. Clamping end to start.
> - Segment 'Action_Handoff' for track '17' has invalid range: start=359, end=83. Clamping end to start.
> - Segment 'Action_BallSnap' for track '19' has invalid range: start=488, end=61. Clamping end to start.
> - Action 'Action_ZoneBlock' range [51-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-558] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-103] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-555] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-289] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-598] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [600-618] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [623-624] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-261] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-498] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-52] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-244] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-629] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-67] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-541] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [549-551] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-313] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [316-322] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [329-348] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-351] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-384] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-540] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-72] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-527] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [529-533] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-537] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-629] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-81] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-483] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-294] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-355] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-341] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [343-494] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-271] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-277] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-316] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-341] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-488] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-214] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-262] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [271-292] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-83] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [231-234] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [247-249] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [254-256] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [258-259] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [266-283] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [292-368] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [376-411] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [417-445] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [459-462] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [471-501] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [519-521] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-345] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-607] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [612-629] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-596] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-599] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-560] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [544-588] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [593-600] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [602-606] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [577-578] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-614] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [584-600] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [597-598] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [607-610] for track '31' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_207'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.