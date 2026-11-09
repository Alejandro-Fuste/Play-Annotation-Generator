# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_108`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_108/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PressEdge' range [102-144] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-166] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-242] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-238] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [113-131] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-196] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-196] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-233] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-256] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-120] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-189] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-189] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-111] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-157] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-112] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-172] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-191] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-257] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-9] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-87] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-114] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-131] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-164] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-169] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-260] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-132] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-145] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-169] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-162] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-195] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-260] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-267] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-251] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-257] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-265] for track '29' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.