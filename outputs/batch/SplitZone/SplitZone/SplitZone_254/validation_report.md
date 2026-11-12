# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_254`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_254/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 510: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '12' has invalid range: start=133, end=17. Clamping end to start.
> - Action 'Action_SplitBlock' range [132-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [187-196] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-245] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-165] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-178] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-229] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-142] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-157] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [159-168] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [181-214] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-149] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-212] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-136] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-196] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-233] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-240] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-389] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [130-179] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-371] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-379] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-161] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-179] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [187-216] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-192] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-213] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-134] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-212] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-27] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-132] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [161-214] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-22] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-14] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-183] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [131-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-156] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-167] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [168-170] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [172-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [222-389] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [135-138] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-152] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-189] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-178] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-190] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-214] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-261] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-286] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-282] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-340] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-361] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-370] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-332] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [348-373] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-377] for track '29' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.