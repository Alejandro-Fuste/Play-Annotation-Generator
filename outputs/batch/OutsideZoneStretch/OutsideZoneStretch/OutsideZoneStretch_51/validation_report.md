# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_51`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 103 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [153-168] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-262] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-275] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [277-285] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-292] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [127-145] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-277] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-204] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-220] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-267] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-221] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-266] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-226] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-295] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-280] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-289] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-254] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-265] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-203] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-148] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [157-171] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-231] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-276] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [282-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-181] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-205] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-245] for track '13' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-135] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-123] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-163] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-213] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-275] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-288] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-249] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-264] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-263] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-289] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-296] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-220] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-299] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-231] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-257] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-221] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-245] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-264] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-240] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-245] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-252] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-280] for track '33' has 1 frames without a visible bounding box.
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