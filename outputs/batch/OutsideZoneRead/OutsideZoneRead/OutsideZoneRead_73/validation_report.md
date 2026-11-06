# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_73`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_73/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 33 |
| Ball Tracks | 1 |
| CSV events parsed | 18 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-40] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-220] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-92] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-110] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-182] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ReadEdgeDefender' range [126-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-151] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-218] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [118-194] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-62] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-203] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-26] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-32] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-105] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-60] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-173] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-147] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-152] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-186] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-147] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-213] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-213] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-232] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '32' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.