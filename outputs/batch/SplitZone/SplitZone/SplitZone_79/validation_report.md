# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_79`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_79/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 124 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 509 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (LG) duration 152 frames exceeds threshold 90 frames [start=279, end=430].
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [276–288], lower_priority='Action_ZoneBlock' annotated_start=279, effective_Action_ZoneBlock_start=289.
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 152 frames exceeds threshold 90 frames [start=279, end=430].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 152 frames exceeds threshold 90 frames [start=279, end=430].
> - Action 'Action_None' range [276-323] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-324] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [330-369] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-440] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-504] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-480] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [483-495] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [497-500] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-322] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-481] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [280-283] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [341-344] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [348-350] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-441] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-473] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [480-482] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [489-494] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-400] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-421] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [424-500] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [276-492] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-326] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-398] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-344] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-357] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [279-292] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [294-297] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [299-300] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [303-334] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [337-339] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [344-430] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [431-476] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [504-505] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-373] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-419] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-442] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [448-451] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-472] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-475] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [300-311] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [316-509] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-384] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-397] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-416] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-509] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [281-300] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [324-330] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [289-306] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [310-311] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [279-284] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [287-295] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [299-301] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [303-304] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [306-358] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-509] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-13] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [279-332] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-360] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-366] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-389] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [398-402] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-406] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-476] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-329] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-368] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-376] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-390] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-364] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-369] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [371-375] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [381-460] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-439] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-462] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [417-509] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [430-431] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-474] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-480] for track '32' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.