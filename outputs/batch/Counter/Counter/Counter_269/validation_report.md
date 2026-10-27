# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_269`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_269/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 540: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Segment 'Action_BallSnap' for track '10' has invalid range: start=246, end=230. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '19' has invalid range: start=246, end=230. Clamping end to start.
> - Action 'Action_None' range [246-343] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-414] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [417-418] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-367] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-353] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-232] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-340] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-391] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-405] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [249-263] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [267-273] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-395] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-401] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-409] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-269] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-275] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-279] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-224] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-235] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [249-260] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-226] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-255] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-291] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-302] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-263] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-407] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-415] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-304] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-327] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-267] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-283] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-316] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-245] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-248] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-291] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' for track '18' starts at frame 249, but the player has no visible bounding box on this frame.
> - Action 'Action_DownBlock' range [249-251] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-330] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-354] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [381-387] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-242] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [256-286] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [255-273] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-316] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-275] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-363] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-371] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-379] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-392] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-395] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-414] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [417-419] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-321] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [320-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-389] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-347] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [332-373] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-389] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-399] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-355] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-391] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-414] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [380-419] for track '35' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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