# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_162`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_162/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 509 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (RG) duration 104 frames exceeds threshold 90 frames [start=281, end=384].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 104 frames exceeds threshold 90 frames [start=281, end=384].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [278–288], lower_priority='Action_ZoneBlock' annotated_start=281, effective_Action_ZoneBlock_start=289.
> - Action 'Action_SplitBlock' range [281-316] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-398] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [400-408] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [410-442] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-344] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-310] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [281-293] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [297-359] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [281-304] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [306-330] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [350-351] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-313] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-325] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [281-332] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [316-492] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [495-497] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-38] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-277] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-283] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-354] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-189] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-224] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-247] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-256] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-277] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-294] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-354] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [281-322] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [289-325] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [328-372] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [385-424] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-231] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-277] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-283] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-506] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-141] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-509] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-238] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-264] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-307] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-315] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-356] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-369] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-500] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [504-509] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-442] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [447-448] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-475] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [374-390] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [389-417] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-447] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-414] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-449] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [455-465] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-405] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-411] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-507] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [399-400] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-410] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [414-509] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-486] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-466] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [424-465] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-474] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-478] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [483-507] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [438-443] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [442-450] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-507] for track '39' has 1 frames without a visible bounding box.
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