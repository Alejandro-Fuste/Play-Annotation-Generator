# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_215`
- **Input XML**: `outputs/batch/Power/Power/Power_215/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Action 'Action_PreSnap' range [30-416] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-350] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-285] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-286] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-407] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [413-414] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-422] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [426-427] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [430-447] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-423] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-260] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [261-279] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-316] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-328] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-310] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-325] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-280] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-285] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-306] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-320] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [333-366] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-420] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [422-423] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [425-441] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-294] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-290] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-277] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-283] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-449] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-348] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-293] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-328] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-439] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-57] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-260] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-342] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [354-360] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-379] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-388] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-196] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-188] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-217] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-303] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [262-264] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-337] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-319] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-325] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-449] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-322] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-408] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-319] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-354] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-372] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-375] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-370] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-449] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-340] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-343] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-349] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-357] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-401] for track '30' has 3 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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