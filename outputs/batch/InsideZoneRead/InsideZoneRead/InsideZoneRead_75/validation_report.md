# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_75`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_75/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Segment 'Action_BallCarry' for track '2' has invalid range: start=255, end=244. Clamping end to start.
> - Segment 'Action_BallSnap' for track '21' has invalid range: start=217, end=47. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '21' has invalid range: start=220, end=47. Clamping end to start.
> - Action 'Action_None' range [217-441] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [443-445] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-430] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-367] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-403] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-396] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-364] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-331] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-398] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [220-286] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [288-295] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-322] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [339-342] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-397] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [220-307] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-322] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-342] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-360] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-380] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-398] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-269] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [272-275] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-293] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-301] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-326] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-326] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-357] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [359-360] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-341] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-414] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-383] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [220-277] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-326] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-351] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-289] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-330] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-405] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-66] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-82] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-89] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-219] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [220-298] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-47] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-71] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-244] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-268] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-412] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-322] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-328] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-449] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-330] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-360] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-362] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [364-380] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-360] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-391] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-369] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-431] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-441] for track '32' has 1 frames without a visible bounding box.
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