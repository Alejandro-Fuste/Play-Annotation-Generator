# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_20`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_20/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 39 |
| Ball Tracks | 1 |
| CSV events parsed | 20 |
| Action Segments inferred | 115 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 42: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 129 frames exceeds threshold 90 frames [start=223, end=351].
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (LG) duration 107 frames exceeds threshold 90 frames [start=223, end=329].
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (RG) duration 129 frames exceeds threshold 90 frames [start=223, end=351].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [220–233], lower_priority='Action_ZoneBlock' annotated_start=223, effective_Action_ZoneBlock_start=234.
> - Segment 'Action_BallCarry' for track '20' has invalid range: start=262, end=255. Clamping end to start.
> - Action 'Action_None' range [220-281] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-323] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [326-330] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-345] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-283] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-318] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-341] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-390] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [393-449] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-262] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-285] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [223-332] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-381] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-17] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-287] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-345] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-449] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-318] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-339] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-347] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-397] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [223-326] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [328-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [223-260] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [264-321] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [352-372] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [374-375] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [223-238] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [249-250] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [270-271] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [274-279] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [289-312] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [220-231] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [258-259] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-199] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-223] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [229-251] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [253-255] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-335] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-327] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-126] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-246] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-266] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-302] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-330] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-365] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-368] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-449] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-385] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-287] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-449] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-313] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [322-332] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [298-305] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [309-325] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-341] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-321] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-328] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [330-397] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-344] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-449] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-352] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-360] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-364] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-399] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-327] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-354] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [369-370] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-421] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [424-435] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [437-439] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-388] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-359] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-363] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-391] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-436] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [439-449] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-374] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-378] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-394] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [402-409] for track '38' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.