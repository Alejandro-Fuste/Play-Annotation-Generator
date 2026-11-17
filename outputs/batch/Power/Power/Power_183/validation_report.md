# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_183`
- **Input XML**: `outputs/batch/Power/Power/Power_183/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [23-362] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-357] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-387] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-259] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-288] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-320] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-419] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-266] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-252] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-261] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-242] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-247] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-419] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-243] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-261] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-304] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-398] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-336] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-316] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-255] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-276] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-248] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-274] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [229-264] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-401] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-402] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [404-408] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-240] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-264] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-276] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-312] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-351] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-274] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-387] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-229] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-255] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-242] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-262] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-308] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-186] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-195] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-223] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-249] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-288] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-413] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-234] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-372] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-37] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [229-243] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [245-246] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [249-266] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-61] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-156] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-228] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [229-237] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [240-243] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [248-254] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [259-261] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-404] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-223] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-276] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-408] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-297] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-301] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-314] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-332] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-387] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-318] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-324] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-357] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-378] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-355] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-360] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-340] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-351] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-381] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-336] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-341] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-375] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-400] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-412] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-419] for track '37' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.