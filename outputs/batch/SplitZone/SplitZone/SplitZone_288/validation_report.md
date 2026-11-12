# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_288`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_288/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 156 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [148–160], lower_priority='Action_ZoneBlock' annotated_start=98, effective_Action_ZoneBlock_start=161.
> - Action 'Action_None' range [148-280] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-254] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-271] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-288] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-389] for track '2' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [148-271] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-192] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-240] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [250-270] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-294] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-305] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-324] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [156-198] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-230] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [232-246] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [256-258] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-270] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-290] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [294-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-311] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-290] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-305] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-310] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-234] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-284] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [290-303] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-205] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-236] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [239-246] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-205] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-240] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [243-246] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-254] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-264] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-389] for track '13' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [148-301] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-236] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-389] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-227] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-278] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [147-197] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-230] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-262] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-351] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [359-369] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-376] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-385] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-206] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-254] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-281] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-353] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-360] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-230] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-246] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-270] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-283] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [214-234] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-261] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-319] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-389] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [190-270] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [273-274] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [282-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [301-329] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [337-341] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [344-345] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-248] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [251-262] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-291] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-389] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-319] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-389] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-320] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [353-357] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-380] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-371] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.