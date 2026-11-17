# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_269`
- **Input XML**: `outputs/batch/Power/Power/Power_269/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-230] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-301] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-316] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-329] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-232] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-300] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-305] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [193-197] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-284] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-291] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-218] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-222] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-266] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-320] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-247] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-278] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-242] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-259] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-245] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-295] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-262] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-289] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-302] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-313] for track '28' has 1 frames without a visible bounding box.
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