# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_228`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_228/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 64 |
| Player Tracks | 64 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 156 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Validation warning: Action 'Action_LeadBlock' for track '15' (TE1) duration 118 frames exceeds threshold 90 frames [start=27, end=144].
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [25–38], lower_priority='Action_ZoneBlock' annotated_start=27, effective_Action_ZoneBlock_start=39.
> - Action 'Action_ZoneBlock' range [27-52] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-67] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-94] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-55] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-45] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-46] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-65] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-52] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-55] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-72] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-49] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-91] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-64] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-92] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-145] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-156] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-172] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-249] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [251-255] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-283] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-297] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-379] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-388] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-404] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-418] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-31] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-40] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-50] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-104] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-152] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-60] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [25-34] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [43-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [22-52] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [57-58] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-62] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-60] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-72] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-71] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-106] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-77] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-253] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-261] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-293] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [296-332] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-198] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [203-224] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-258] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-288] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-337] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [341-342] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-348] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-93] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-173] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-154] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-149] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-140] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-245] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-171] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-249] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-283] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-266] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-216] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [219-235] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-249] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-220] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-253] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-284] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-181] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-207] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-419] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-200] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-204] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-247] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-256] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-305] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-240] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-242] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-252] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-243] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-304] for track '47' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [316-388] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-338] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [342-347] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-251] for track '49' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [253-292] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-272] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-298] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-290] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-305] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-344] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [348-354] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-329] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-417] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-380] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-368] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-399] for track '59' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [403-416] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-419] for track '60' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [391-393] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-399] for track '63' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.