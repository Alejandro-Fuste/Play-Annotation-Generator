# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_122`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_122/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 52 |
| Player Tracks | 51 |
| Ball Tracks | 1 |
| CSV events parsed | 15 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '11' has invalid range: start=38, end=36. Clamping end to start.
> - Action 'Action_PreSnap' range [0-137] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-168] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-184] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-389] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-249] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-254] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-306] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-310] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-389] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-41] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [46-47] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-50] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-95] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-126] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-136] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-94] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-54] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-343] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-244] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-61] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-71] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-94] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-108] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [38-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [43-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [46-48] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [55-101] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [104-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [108-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-109] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-128] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-75] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-141] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-79] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-89] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-98] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-117] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-124] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-127] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-146] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-136] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-246] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-148] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-389] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-200] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-244] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-243] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-246] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-271] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-243] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-255] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-274] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-293] for track '41' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-292] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-355] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-311] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-322] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-335] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-340] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-335] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-369] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-384] for track '50' has 2 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.