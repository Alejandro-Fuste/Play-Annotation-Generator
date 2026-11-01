# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_115`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_115/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 689 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 232: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
> - Segment 'Action_BallCarry' for track '13' has invalid range: start=602, end=590. Clamping end to start.
> - Segment 'Action_BallSnap' for track '21' has invalid range: start=568, end=231. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '21' has invalid range: start=571, end=231. Clamping end to start.
> - Action 'Action_None' range [568-683] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-689] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-680] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [571-612] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-244] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-255] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [571-634] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-637] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [639-689] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-590] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-427] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [571-615] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [623-626] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-408] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [411-413] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-474] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-588] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [593-632] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [635-636] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [641-642] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-55] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-243] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-228] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-243] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-254] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-652] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [659-661] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [676-689] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-311] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-317] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-343] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-364] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-380] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [382-393] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [400-401] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [421-429] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [440-567] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-613] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [568-598] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [603-618] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [597-605] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [636-683] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [642-664] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [669-684] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [652-659] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [662-667] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [676-677] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [671-673] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [684-685] for track '31' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.