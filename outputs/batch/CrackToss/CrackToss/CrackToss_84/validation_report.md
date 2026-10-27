# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_84`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_84/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 374 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 374 as fallback play end.
> - Segment 'Action_BallSnap' for track '12' has invalid range: start=241, end=116. Clamping end to start.
> - Action 'Action_None' range [241-278] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-318] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-336] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-266] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-362] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-369] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [244-328] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-256] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-274] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-279] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-306] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-343] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-349] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-359] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [272-325] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-276] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-328] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-240] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-306] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-346] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-122] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-278] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-258] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-320] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-12] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-15] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-24] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-99] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-111] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-258] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-374] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-34] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-286] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-301] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [244-261] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-333] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-358] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [248-328] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-366] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-374] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-374] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-283] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-332] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-318] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-313] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-316] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-320] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-326] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-372] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-351] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-355] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.