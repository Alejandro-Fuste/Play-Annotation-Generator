# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_3`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 388 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 388 as fallback play end.
> - Segment 'Action_ComboBlock' for track '9' has invalid range: start=236, end=229. Clamping end to start.
> - Segment 'Action_ComboBlock' for track '21' has invalid range: start=236, end=233. Clamping end to start.
> - Action 'Action_PreSnap' range [0-388] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-384] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-323] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-388] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-323] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-388] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-381] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-255] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-362] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-371] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [236-305] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-315] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [320-371] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-313] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-370] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [383-386] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-229] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-240] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-367] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-371] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [260-320] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [323-333] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [337-388] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-265] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-303] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-325] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-362] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-371] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-337] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-280] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-294] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-301] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-310] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [377-378] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-384] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-291] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-300] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-388] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-362] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-377] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-279] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-233] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-308] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-316] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-281] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-285] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-289] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-301] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-275] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-285] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-332] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-371] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-317] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-320] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-323] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-387] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-338] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-333] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-345] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-337] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-348] for track '31' has 1 frames without a visible bounding box.
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