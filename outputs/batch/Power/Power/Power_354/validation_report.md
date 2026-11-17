# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_354`
- **Input XML**: `outputs/batch/Power/Power/Power_354/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [22-275] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-215] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-60] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-78] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-295] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-207] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-240] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-247] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-243] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-247] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-252] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-286] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-289] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-299] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [175-194] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-256] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-265] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-255] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-277] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [175-199] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [201-202] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-238] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-278] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-292] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-170] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-213] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-174] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [175-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-278] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-279] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-133] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-140] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-158] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-265] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-197] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-269] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-228] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-255] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-270] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-273] for track '21' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.