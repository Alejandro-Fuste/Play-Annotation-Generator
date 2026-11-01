# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_61`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_61/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (LG) duration 91 frames exceeds threshold 90 frames [start=215, end=305].
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (LT) duration 91 frames exceeds threshold 90 frames [start=215, end=305].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 91 frames exceeds threshold 90 frames [start=215, end=305].
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [212–224], lower_priority='Action_ZoneBlock' annotated_start=215, effective_Action_ZoneBlock_start=225.
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 91 frames exceeds threshold 90 frames [start=215, end=305].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 91 frames exceeds threshold 90 frames [start=215, end=305].
> - Action 'Action_None' range [212-400] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-437] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-442] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-509] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [518-525] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [532-536] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [540-600] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-250] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-357] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-629] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-520] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-629] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [255-313] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-329] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [212-312] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-626] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [255-465] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-458] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-468] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-436] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-441] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-255] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-326] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-629] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-41] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [215-295] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [297-305] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-519] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-42] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-72] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-455] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-332] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [320-399] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-379] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-405] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-414] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-412] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-427] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-431] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.