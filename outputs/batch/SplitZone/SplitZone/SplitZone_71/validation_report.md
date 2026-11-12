# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_71`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_71/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [202–215], lower_priority='Action_ZoneBlock' annotated_start=205, effective_Action_ZoneBlock_start=216.
> - Action 'Action_None' range [202-238] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-302] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-229] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-261] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-270] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-379] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-368] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-250] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-276] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-308] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-312] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-388] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [205-251] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-325] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-380] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-276] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-289] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-262] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-316] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-323] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-332] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-265] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-285] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-279] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-386] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [247-265] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-329] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-336] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-330] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-339] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [345-353] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [334-336] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-349] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-362] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [372-376] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-381] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [384-389] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [382-384] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-389] for track '30' has 1 frames without a visible bounding box.
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