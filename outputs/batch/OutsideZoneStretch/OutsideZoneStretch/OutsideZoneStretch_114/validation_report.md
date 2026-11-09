# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_114`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_114/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 230: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-223] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-324] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-251] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-328] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-188] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-199] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-212] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-217] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-61] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-109] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-176] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-193] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-307] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-223] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-232] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-315] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-248] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-206] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-246] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-326] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-158] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-246] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-270] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-286] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-292] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-255] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-143] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-245] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-183] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-243] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-179] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-219] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-217] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-258] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-295] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-267] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-274] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-288] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-288] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-287] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-280] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-284] for track '30' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.