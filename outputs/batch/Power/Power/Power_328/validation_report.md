# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_328`
- **Input XML**: `outputs/batch/Power/Power/Power_328/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [27-311] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [226-272] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-286] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-306] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-225] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-291] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [293-318] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-297] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-338] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-320] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-305] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-300] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-252] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-234] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-228] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-359] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-31] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-347] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-229] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-266] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-270] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-285] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-222] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-356] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-288] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-280] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-312] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-340] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-320] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-342] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-356] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-323] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-337] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-329] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-315] for track '26' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.