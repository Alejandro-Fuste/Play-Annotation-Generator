# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_175`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_175/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 143 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [180–193], lower_priority='Action_ZoneBlock' annotated_start=183, effective_Action_ZoneBlock_start=194.
> - Action 'Action_None' range [180-299] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [180-312] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-319] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-323] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-321] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-334] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-340] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-347] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-360] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-380] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-297] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-312] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-337] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-360] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [363-364] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-369] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [214-385] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-221] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-312] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-319] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-326] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-343] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [346-365] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [367-371] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-385] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-312] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-302] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [306-308] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-378] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [380-389] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-389] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 264, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [264-264] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-225] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-247] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-302] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [306-311] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-316] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-321] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-348] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-354] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-370] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-380] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-241] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-350] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-359] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [362-366] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-376] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-276] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-296] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-9] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-12] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-179] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-263] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-337] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-182] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [183-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [225-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-291] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-300] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-312] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-324] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-330] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-350] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-359] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-368] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-11] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [183-200] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-78] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [183-197] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-226] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-255] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-299] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [255-267] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-297] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [304-318] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [321-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-389] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-299] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-313] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-350] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-360] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-383] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-388] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-300] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-304] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-332] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-389] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-343] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-375] for track '32' has 1 frames without a visible bounding box.
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