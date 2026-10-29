# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_8`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 26 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 358 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
> - Action 'Action_BallCarry' range [221-262] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [265-336] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-258] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-257] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-265] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-270] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [195-198] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [201-205] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [218-221] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-272] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-358] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [195-207] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [211-224] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-282] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-263] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-323] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-262] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [195-234] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [236-245] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-258] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-251] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-262] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-247] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-270] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-275] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [223-246] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-274] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-230] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-267] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-87] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-174] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-289] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-353] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-352] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.