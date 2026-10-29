# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_13`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_13/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 358 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 28: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
> - Action 'Action_PreSnap' range [0-304] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-340] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-358] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [246-358] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [256-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [271-272] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-254] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-259] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-275] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-280] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-287] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-295] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-308] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-358] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-303] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-320] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-325] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-285] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-358] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-290] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-321] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-325] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [228-229] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [236-237] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [249-254] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [228-230] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [232-295] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-227] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [228-275] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [285-293] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-280] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-218] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [238-243] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-345] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-229] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-235] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-249] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-256] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-304] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-342] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-267] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-305] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-311] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-343] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-358] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-332] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-358] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-358] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-358] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-321] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-321] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-334] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-355] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-358] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-358] for track '32' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.