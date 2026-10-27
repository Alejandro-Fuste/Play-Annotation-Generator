# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_20`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_20/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 29 |
| Ball Tracks | 2 |
| CSV events parsed | 20 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '10' (LB2) duration 104 frames exceeds threshold 90 frames [start=203, end=306].
> - Action 'Action_None' range [200-292] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-298] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-344] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-346] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-349] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-353] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-357] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-243] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-259] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-356] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [200-281] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [283-285] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [203-241] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [243-246] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-271] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-222] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-291] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-344] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [348-349] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-265] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-233] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-250] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-87] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-127] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-141] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-194] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-232] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-217] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-311] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-343] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-359] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-328] for track '30' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.