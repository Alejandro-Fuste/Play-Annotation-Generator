# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_141`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_141/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 121 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 659 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
> - Validation warning: Action 'Action_BlockSecondLevel' for track '1' (TE1) duration 125 frames exceeds threshold 90 frames [start=454, end=578].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 149 frames exceeds threshold 90 frames [start=430, end=578].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 149 frames exceeds threshold 90 frames [start=430, end=578].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [427–439], lower_priority='Action_ZoneBlock' annotated_start=430, effective_Action_ZoneBlock_start=440.
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 99 frames exceeds threshold 90 frames [start=430, end=528].
> - Action 'Action_SplitBlock' range [433-551] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [454-480] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [579-631] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [634-635] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-484] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-573] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [575-659] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [427-636] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [646-655] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-612] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [614-659] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [427-467] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [465-649] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-516] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-543] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-561] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-659] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [579-633] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [427-659] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-516] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [522-659] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-169] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-486] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [430-507] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-24] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-45] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-63] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-76] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-87] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-127] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [430-458] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [460-461] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-37] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-40] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-59] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-429] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [430-528] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-123] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-197] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-240] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-259] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-313] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [456-475] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [477-586] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-491] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [484-486] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [496-515] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [536-539] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-607] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [560-565] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [569-578] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [580-583] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [585-586] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [619-620] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [624-632] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [634-635] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [573-576] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [588-589] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [591-592] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [596-597] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [608-616] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [618-621] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [624-625] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [627-632] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [634-635] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [644-645] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [647-649] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [651-653] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [611-612] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [615-621] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [624-626] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [625-628] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [634-635] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [644-645] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [644-647] for track '41' has 1 frames without a visible bounding box.
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
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.