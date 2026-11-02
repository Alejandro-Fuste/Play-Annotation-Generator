# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_76`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_76/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 42 |
| Ball Tracks | 1 |
| CSV events parsed | 25 |
| Action Segments inferred | 122 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [102–112], lower_priority='Action_ZoneBlock' annotated_start=103, effective_Action_ZoneBlock_start=113.
> - Action 'Action_None' range [102-319] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [103-196] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [199-205] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [207-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [219-225] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [227-419] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-319] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [103-189] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-205] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-237] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-277] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-321] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-139] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-163] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-419] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [102-315] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-419] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [132-357] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [359-388] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [392-398] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [403-412] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [418-419] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-159] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-188] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-139] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-419] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-191] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-321] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-196] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-286] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-366] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-257] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-286] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-351] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-390] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-137] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-357] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [360-392] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-260] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-143] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [151-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-137] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [139-172] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-204] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-419] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-358] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-225] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-345] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-321] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-322] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-332] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-341] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-365] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-342] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-362] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-373] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-369] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-406] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-382] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-390] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-399] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-412] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [399-402] for track '42' has 1 frames without a visible bounding box.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.